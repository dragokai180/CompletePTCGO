from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7a1f74e4-db8d-56e0-8574-6c479afa8442',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spinda.Name',
    display_name='Spinda',
    searchable_by=['Spinda', 'Basic', 'Spinda'],
    subtypes=['Basic'],
    collector_number=102,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=327,
    abilities=[
        Attack(
            title='Teeter Punch',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
