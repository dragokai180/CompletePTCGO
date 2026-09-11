from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cfe08784-d6e3-522f-86aa-ba4d2a6ec6e4',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lokix.Name',
    display_name='Lokix',
    searchable_by=['Lokix', 'Stage 1', 'Lokix'],
    subtypes=['Stage 1'],
    collector_number=122,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name',
    family_id=919,
    abilities=[
        Attack(
            title='Bounce',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Punishing Kick',
            game_text="This attack does 40 more damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
