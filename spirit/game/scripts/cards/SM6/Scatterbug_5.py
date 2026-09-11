from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b9556713-cd9e-5f74-9e89-d77af5546aca',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name',
    display_name='Scatterbug',
    searchable_by=['Scatterbug', 'Basic', 'Scatterbug'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=664,
    abilities=[
        Ability(
            title='Abnormal Outbreak',
            game_text='You can use this Ability only if you go second. Once during your first turn (before your attack), you may search your deck for a Spewpa and a Vivillon, reveal them, and put them into your hand. Then, shuffle your deck.',
            passive=standard_passive('You can use this Ability only if you go second. Once during your first turn (before your attack), you may search your deck for a Spewpa and a Vivillon, reveal them, and put them into your hand. Then, shuffle your deck.'),
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
        ),
    ],
)
