from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
    hyper_transfer, hyper_transfer_condition,
)


card = PokemonCardDef(
    guid='ee6534f9-9946-519d-ad86-4aa20a8280e1',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GolduckBREAK.Name',
    display_name='Golduck BREAK',
    searchable_by=['Golduck BREAK', 'BREAK', 'GolduckBREAK'],
    subtypes=['BREAK'],
    collector_number=18,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name',
    family_id=54,
    abilities=[
        Ability(
            title='Hyper Transfer',
            game_text='As often as you like during your turn (before your attack), you may move a basic Energy from 1 of your Pokémon to another of your Pokémon.',
            effect=hyper_transfer,
            condition=hyper_transfer_condition,
            activation=Activations.UNLIMITED,
        ),
    ],
)
