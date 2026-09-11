from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ca7c6cb6-3645-52fa-b12b-93053aac4cee',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name',
    display_name='Rotom',
    searchable_by=['Rotom', 'Basic', 'Rotom'],
    subtypes=['Basic'],
    collector_number=20,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    family_id=479,
    abilities=[
        Ability(
            title='Mischievous Trick',
            game_text="Once during your turn (before your attack), you may switch 1 of your face-down Prize cards with the top card of your deck. This power can't be used if Rotom is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Plasma Arrow',
            game_text="Choose 1 of your opponent's Pokémon. This attack does 20 damage for each Energy attached to that Pokémon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
    ],
)
