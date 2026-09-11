from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='727a83e6-723a-5668-b890-1437a78e0cf5',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoEX.Name',
    display_name='Mewtwo-EX',
    searchable_by=['Mewtwo-EX', 'Basic', 'EX', 'MewtwoEX'],
    subtypes=['Basic', 'EX'],
    collector_number=52,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=150,
    abilities=[
        Attack(
            title='Energy Absorption',
            game_text='Attach an Energy card from your discard pile to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Regeneration',
            game_text='Heal 60 damage from this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psyburn',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=110,
        ),
    ],
)
