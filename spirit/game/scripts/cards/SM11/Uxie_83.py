from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d4615668-4545-520a-bd8b-867700ba7c28',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Uxie.Name',
    display_name='Uxie',
    searchable_by=['Uxie', 'Basic', 'Uxie'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=480,
    abilities=[
        Ability(
            title='Secret Territory',
            game_text="If you have Mesprit and Azelf in play, apply Weakness for each Pokémon (both yours and your opponent's) as ×4 instead.",
            passive=standard_passive("If you have Mesprit and Azelf in play, apply Weakness for each Pokémon (both yours and your opponent's) as ×4 instead."),
        ),
        Attack(
            title='Psyshot',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
