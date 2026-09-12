from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.trainers import is_basic_energy_card

async def energy_wheel(ctx):
    bench = ctx.my_bench()
    energies = [energy for pokemon in bench for energy in ctx.attached_energies(pokemon)]
    if not bench or not energies:
        return
    picked = await ctx.choose_cards(energies, 1, minimum=1, prompt="Choose an Energy to move")
    if not picked:
        return
    await ctx.move_energy(picked[0], ctx.attacker)


async def hurricane(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = [energy for energy in ctx.attached_energies(ctx.attacker)
                if is_basic_energy_card(energy)]
    if bench and energies:
        picked = await ctx.choose_cards(energies, 1, minimum=1,
                                       prompt="Choose a basic Energy to move")
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon")
        if picked and target is not None:
            await ctx.move_energy(picked[0], target)



card = PokemonCardDef(
    guid="54689dba-f787-5d3f-9762-d305d6d4b1f6",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tornadus.Name",
    display_name="Tornadus",
    searchable_by=["Tornadus","Basic","Tornadus"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="BW2",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Energy Wheel",
            game_text="Move an Energy from 1 of your Benched Pokémon to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=energy_wheel,
        ),
        Attack(
            title="Hurricane",
            game_text="Move a basic Energy from this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=hurricane,
        ),
    ],
)
