from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e2394dde-b4e7-5a80-9554-43e1aed781ae',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name',
    display_name='Croconaw',
    searchable_by=['Croconaw', 'Stage 1', 'Croconaw'],
    subtypes=['Stage 1'],
    collector_number=19,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name',
    family_id=158,
    abilities=[
        Ability(
            title='Plunge',
            game_text='Once during your turn (before your attack), if this Pokémon is on your Bench, you may move all Energy from your Active Pokémon to this Pokémon. If you do, switch it with your Active Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
