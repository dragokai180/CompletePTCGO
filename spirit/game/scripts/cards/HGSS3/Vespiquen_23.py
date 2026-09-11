from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8c4969f8-5ca7-5394-bb96-f3cd43fa8b3f',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquen.Name',
    display_name='Vespiquen',
    searchable_by=['Vespiquen', 'Stage 1', 'Vespiquen'],
    subtypes=['Stage 1'],
    collector_number=23,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name',
    family_id=415,
    abilities=[
        Ability(
            title='Defense Sign',
            game_text='Prevent all damage done to your Benched Grass Pokémon by attacks.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('Prevent all damage done to your Benched Grass Pokémon by attacks.'),
        ),
        Attack(
            title='Mach Wind',
            game_text="During your next turn, Vespiquen's Retreat Cost is 0.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
