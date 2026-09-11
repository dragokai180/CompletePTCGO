from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0c8b890b-78dc-589c-99ac-9e0a046d183d',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name',
    display_name='Deoxys',
    searchable_by=['Deoxys', 'Basic', 'Deoxys'],
    subtypes=['Basic'],
    collector_number=67,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=386,
    abilities=[
        Attack(
            title='Psychic',
            game_text="This attack does 20 more damage times the amount of Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Power Blast',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
