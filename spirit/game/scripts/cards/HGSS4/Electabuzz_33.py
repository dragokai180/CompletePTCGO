from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='56edd472-ebb9-55b5-bb77-fe6b4e1ea540',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name',
    display_name='Electabuzz',
    searchable_by=['Electabuzz', 'Basic', 'Electabuzz'],
    subtypes=['Basic'],
    collector_number=33,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=125,
    abilities=[
        Attack(
            title='Light Punch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Shock Bolt',
            game_text='Flip a coin. If tails, discard all Lightning Energy attached to Electabuzz.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
