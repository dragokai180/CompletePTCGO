from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="31acfa0b-a715-5ff6-8db8-15e41cfa6205",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsJoltik.Name",
    display_name="N's Joltik",
    searchable_by=["N's Joltik", "Basic", "NsJoltik"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=595,
    abilities=[
        Attack(
            title="Zapping Short",
            game_text="Before doing damage, discard all Pokémon Tools from your opponent's Active Pokémon. If you discarded a Pokémon Tool in this way, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
