from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import discard_own_energy

card = PokemonCardDef(
    guid="105dcdc2-8018-5754-98f6-68c19a82bc58",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name",
    display_name="Tranquill",
    searchable_by=["Tranquill","Stage 1","Tranquill"],
    subtypes=["Stage 1"],
    collector_number=124,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidove.Name",
    abilities=[
        Attack(
            title="Air Slash",
            game_text="Discard an Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=discard_own_energy,
        ),
    ],
)
