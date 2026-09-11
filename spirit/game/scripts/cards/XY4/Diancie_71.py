from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='96ad0e44-d289-5b19-b6fa-b46fd79834e1',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Diancie.Name',
    display_name='Diancie',
    searchable_by=['Diancie', 'Basic', 'Diancie'],
    subtypes=['Basic'],
    collector_number=71,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=719,
    abilities=[
        Attack(
            title='Sparkle',
            game_text="If the Defending Pokémon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Diamond Storm',
            game_text='Heal 30 damage from each of your Fairy Pokémon.',
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
