from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e46b37c3-8309-518d-bf51-d2c9859b28dd',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Swellow.Name',
    display_name='Swellow',
    searchable_by=['Swellow', 'Stage 1', 'Swellow'],
    subtypes=['Stage 1'],
    collector_number=103,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Taillow.Name',
    family_id=276,
    abilities=[
        Ability(
            title='Drive Off',
            game_text='Once during your turn (before your attack), you may have your opponent switch his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Wing Attack',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)
