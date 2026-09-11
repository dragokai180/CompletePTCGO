from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d39c59ad-ac00-519c-b16f-f7276bbdc467',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraGX.Name',
    display_name='Zeraora-GX',
    searchable_by=['Zeraora-GX', 'Basic', 'GX', 'ZeraoraGX'],
    subtypes=['Basic', 'GX'],
    collector_number=86,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=807,
    abilities=[
        Ability(
            title='Thunderclap Zone',
            game_text='Each of your Pokémon that has any Lightning Energy attached to it has no Retreat Cost.',
            passive=standard_passive('Each of your Pokémon that has any Lightning Energy attached to it has no Retreat Cost.'),
        ),
        Attack(
            title='Plasma Fists',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
        Attack(
            title='Full Voltage-GX',
            game_text="Attach 5 basic Energy cards from your discard pile to your Pokémon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
