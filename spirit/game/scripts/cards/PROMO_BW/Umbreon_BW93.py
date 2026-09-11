from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import blazing_claws, dark_clamp, leech_life, solar_transporter, steamroll

card = PokemonCardDef(
    guid="e2234c68-8d01-5d4a-a8da-7863c5b7036f",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon","Stage 1","Umbreon"],
    subtypes=["Stage 1"],
    collector_number=93,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    abilities=[
        Attack(
            title="Shadow Drain",
            game_text="Heal from this Pokémon the same amount of damage you did to the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=leech_life,
        ),
        Attack(
            title="Slashing Strike",
            game_text="This Pokémon can't use Slashing Strike during your next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            locks_next_turn=True,
        ),
    ],
)
