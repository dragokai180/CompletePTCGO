from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a7272b6d-8384-5391-85bf-246f382baf02',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lokix.Name',
    display_name='Lokix',
    searchable_by=['Lokix', 'Stage 1', 'Lokix'],
    subtypes=['Stage 1'],
    collector_number=21,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name',
    family_id=919,
    abilities=[
        Attack(
            title='Assaulting Kick',
            game_text='If this Pokémon evolved from Nymble during this turn, this attack does 100 more damage.',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Speed Attack',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
