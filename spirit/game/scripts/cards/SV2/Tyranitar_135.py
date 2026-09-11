from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='da42c29b-5da5-511a-b715-8f954e5d7a12',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name',
    display_name='Tyranitar',
    searchable_by=['Tyranitar', 'Stage 2', 'Tyranitar'],
    subtypes=['Stage 2'],
    collector_number=135,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name',
    family_id=246,
    abilities=[
        Attack(
            title='Rout',
            game_text="This attack does 30 more damage for each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Dread Mountain',
            game_text='Discard the top 4 cards of your deck.',
            cost={PokemonTypes.DARKNESS: 2},
            damage=230,
            effect=standard_attack,
        ),
    ],
)
