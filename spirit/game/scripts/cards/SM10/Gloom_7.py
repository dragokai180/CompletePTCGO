from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3cb8c184-8750-5ad6-86d2-68ca37a48d5e',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name',
    display_name='Gloom',
    searchable_by=['Gloom', 'Stage 1', 'Gloom'],
    subtypes=['Stage 1'],
    collector_number=7,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name',
    family_id=43,
    abilities=[
        Ability(
            title='Irresistible Aroma',
            game_text="Once during your turn (before your attack), if your opponent's Bench isn't full, you may flip a coin. If heads, your opponent reveals their hand. Put a Basic Pokémon you find there onto their Bench.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Drool',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
