from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="faedccb4-b724-5d43-98fa-92077f02e26c",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skeledirge.Name",
    display_name="Skeledirge",
    searchable_by=["Skeledirge", "Stage 2", "Skeledirge"],
    subtypes=["Stage 2"],
    collector_number=31,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name",
    family_id=909,
    abilities=[
        Ability(
            title="Unaware",
            game_text="Prevent all effects of attacks used by your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)",
            passive=standard_passive("Prevent all effects of attacks used by your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)"),
        ),
        Attack(
            title="Torcherto",
            game_text="This attack does 20 more damage for each Benched Pokémon (both yours and your opponent's).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
