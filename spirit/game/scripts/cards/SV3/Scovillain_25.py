from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f648e738-19a9-573d-82f9-30b003807972',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scovillain.Name',
    display_name='Scovillain',
    searchable_by=['Scovillain', 'Stage 1', 'Scovillain'],
    subtypes=['Stage 1'],
    collector_number=25,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name',
    family_id=951,
    abilities=[
        Ability(
            title='Double Type',
            game_text='As long as this Pokémon is in play, it is Grass and Fire type.',
            passive=standard_passive('As long as this Pokémon is in play, it is Grass and Fire type.'),
        ),
        Attack(
            title='Spicy Headbutt',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
