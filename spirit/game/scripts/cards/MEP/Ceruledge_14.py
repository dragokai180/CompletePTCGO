from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="f5133222-02d1-545c-8bd1-1b1999437aec",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ceruledge.Name",
    display_name="Ceruledge",
    searchable_by=["Ceruledge", "Stage 1", "Ceruledge"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    abilities=[
        Attack(
            title="Infernal Slash",
            game_text="Discard 4 Basic [ [Fire] ] Energy cards from your hand. If you can't discard 4 cards in this way, this attack does nothing.",
            cost={PokemonTypes.FIRE: 1},
            damage=220,
            effect=standard_attack,
        ),
    ],
)
