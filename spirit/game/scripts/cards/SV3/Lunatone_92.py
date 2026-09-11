from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9a770f36-2dae-5bdf-a2f9-c7a7b66a30d7',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name',
    display_name='Lunatone',
    searchable_by=['Lunatone', 'Basic', 'Lunatone'],
    subtypes=['Basic'],
    collector_number=92,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=337,
    abilities=[
        Ability(
            title='New Moon',
            game_text='If you have Solrock in play, prevent all effects of any Stadium done to your Pokémon in play.',
            passive=standard_passive('If you have Solrock in play, prevent all effects of any Stadium done to your Pokémon in play.'),
        ),
        Attack(
            title='Moon Press',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
