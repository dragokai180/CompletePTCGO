from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d921fe32-5fcd-5bd8-aae5-19a8aa9b7b6f',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shroodle.Name',
    display_name='Shroodle',
    searchable_by=['Shroodle', 'Basic', 'Shroodle'],
    subtypes=['Basic'],
    collector_number=99,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=944,
    abilities=[
        Attack(
            title='Scratch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Toxic Teeth',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
