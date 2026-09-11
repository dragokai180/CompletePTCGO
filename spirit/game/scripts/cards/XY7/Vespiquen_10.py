from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3405e964-9005-5d8f-a219-84d09660d31c',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquen.Name',
    display_name='Vespiquen',
    searchable_by=['Vespiquen', 'Stage 1', 'Vespiquen'],
    subtypes=['Stage 1'],
    collector_number=10,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name',
    family_id=415,
    abilities=[
        Attack(
            title='Intelligence Gathering',
            game_text='You may draw cards until you have 6 cards in your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Bee Revenge',
            game_text='This attack does 10 more damage for each Pokémon in your discard pile.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
