from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b62eba0b-6363-5703-bbae-3d415518b972',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name',
    display_name='Typhlosion',
    searchable_by=['Typhlosion', 'Stage 2', 'Prime', 'Typhlosion'],
    subtypes=['Stage 2', 'Prime'],
    collector_number=9,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'HGSS09'}},
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name',
    family_id=157,
    abilities=[
        Ability(
            title='Afterburner',
            game_text="Once during your turn (before your attack), you may search your discard pile for a Fire Energy card and attach it to 1 of your Pokémon. If you do, put 1 damage counter on that Pokémon. This power can't be used if Typhlosion is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Flare Destroy',
            game_text='Discard an Energy card attached to Typhlosion and discard an Energy card attached to the Defending Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
