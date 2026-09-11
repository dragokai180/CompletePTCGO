from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bde1aa5b-59c7-51c9-8207-186abc447716',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sawsbuck.Name',
    display_name='Sawsbuck',
    searchable_by=['Sawsbuck', 'Stage 1', 'Sawsbuck'],
    subtypes=['Stage 1'],
    collector_number=16,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Deerling.Name',
    family_id=585,
    abilities=[
        Ability(
            title='Seasonal Blessings',
            game_text='Once during your turn (before your attack), you may draw a card.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Bounce',
            game_text='You may switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
