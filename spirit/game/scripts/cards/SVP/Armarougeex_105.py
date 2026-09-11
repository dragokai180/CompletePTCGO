from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="168f8b1a-3b9e-56b1-889c-a5f87d1a5b3c",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armarougeex.Name",
    display_name="Armarouge ex",
    searchable_by=["Armarouge ex", "Stage 1", "ex", "Armarougeex"],
    subtypes=["Stage 1", "ex"],
    collector_number=105,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=260,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=936,
    abilities=[
        Attack(
            title="Armor Cannon",
            game_text="Discard a Fire Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
