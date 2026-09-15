from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.trainers import is_basic_energy_card

async def energy_wheel(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = ctx.attached_energies(ctx.attacker)
    if not bench or not energies:
        return
    picked = await ctx.choose_cards(energies, 1, minimum=1, prompt="Choose an Energy to move")
    if not picked:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the Benched Pokémon to move the Energy to"
    )
    if target is not None:
        await ctx.move_energy(picked[0], target)


async def hurricane(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench:
        await ctx.move_energy_freely(
            [ctx.attacker], bench, predicate=is_basic_energy_card, max_count=1,
            prompt="Choose a basic Energy to move to a Benched Pokémon",
        )



card = PokemonCardDef(
    guid="32820dcc-2e97-5b4a-8b0b-8bd5b6577fe5",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tornadus.Name",
    display_name="Tornadus",
    searchable_by=["Tornadus","Basic","Tornadus"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="BW2",
    rarity=Rarities.RareUltra,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
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
