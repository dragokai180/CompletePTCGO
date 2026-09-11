from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="e876a54d-a13d-5c44-853d-3504eaf4852b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansMagcargo.Name",
    display_name="Ethan's Magcargo",
    searchable_by=["Ethan's Magcargo", "Stage 1", "EthansMagcargo"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.EthansSlugma.Name",
    family_id=218,
    abilities=[
        Ability(
            title="Melt Away",
            game_text="If this Pokémon has no Energy attached, it has no Retreat Cost.",
            passive=standard_passive("If this Pokémon has no Energy attached, it has no Retreat Cost."),
        ),
        Attack(
            title="Lava Burst",
            game_text="Discard up to 5 Fire Energy from this Pokémon. This attack does 70 damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 3},
            damage=70,
            damage_operator="x",
            effect=standard_attack,
        ),
    ],
)
