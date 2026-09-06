from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on

card = PokemonCardDef(
    guid="9324508c-ea7d-54fc-96e9-7df2e1191245",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsReshiram.Name",
    display_name="N's Reshiram",
    searchable_by=["N's Reshiram", "Basic", "NsReshiram"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=643,
    abilities=[
        Attack(
            title="Powerful Rage",
            game_text="This attack does 20 damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(damage_counters_on("self"), 20),
        ),
        Attack(
            title="Virtuous Flame",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=170,
        ),
    ],
)
