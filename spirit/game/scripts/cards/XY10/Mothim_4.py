from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='364d0364-661b-56cd-b813-732258b681f4',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mothim.Name',
    display_name='Mothim',
    searchable_by=['Mothim', 'Stage 1', 'Mothim'],
    subtypes=['Stage 1'],
    collector_number=4,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Burmy.Name',
    family_id=412,
    abilities=[
        Ability(
            title='Wormadam First',
            game_text='As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your Wormadam to another of your Pokémon.',
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Gust',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)
