from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='48b90675-78b2-502c-a927-a7388df03590',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name',
    display_name='Magcargo',
    searchable_by=['Magcargo', 'Stage 1', 'Magcargo'],
    subtypes=['Stage 1'],
    collector_number=6,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name',
    family_id=218,
    abilities=[
        Attack(
            title='Searing Flame',
            game_text='The Defending Pokémon is now Burned.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Lava Flow',
            game_text='You may discard any number of Fire Energy cards attached to Magcargo. If you do , this attack does 60 damage plus 20 more damage for each Fire Energy card you discarded.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
