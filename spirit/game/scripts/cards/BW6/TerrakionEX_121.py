from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.bw10 import shadow_punch, sinister_hand, sinister_hand_condition
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.trainers import is_basic_energy_card

async def pump_up_smash(ctx):
    await ctx.deal_damage()
    energies = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=0,
        prompt="Choose up to 2 basic Energy cards to attach to your Pokémon",
    )
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())



card = PokemonCardDef(
    guid="5f3cfa72-2b29-5d75-8721-bcf26f454db2",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TerrakionEX.Name",
    display_name="Terrakion-EX",
    searchable_by=["Terrakion-EX","Basic","EX","TerrakionEX"],
    subtypes=["Basic","EX"],
    collector_number=121,
    set_code="BW6",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    abilities=[
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=shadow_punch,
        ),
        Attack(
            title="Pump-up Smash",
            game_text="Attach 2 basic Energy cards from your hand to your Benched Pokémon in any way you like.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=pump_up_smash,
        ),
    ],
)
