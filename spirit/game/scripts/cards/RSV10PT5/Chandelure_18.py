from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="4e80fb6a-a597-5204-886c-3f20579c5adf",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name",
    display_name="Chandelure",
    searchable_by=["Chandelure", "Stage 2", "Chandelure"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Attack(
            title="Incendiary Pillar",
            game_text="If you have 10 or more Basic Fire Energy cards in your discard pile, this attack does 100 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Burn It All Up",
            game_text="Discard all Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=180,
            effect=standard_attack,
        ),
    ],
)
