from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b4ac947f-c56e-5207-b6f4-75692f74ef56',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name',
    display_name='Dunsparce',
    searchable_by=['Dunsparce', 'Basic', 'Dunsparce'],
    subtypes=['Basic'],
    collector_number=41,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=206,
    abilities=[
        Attack(
            title='Glare',
            game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fade Out',
            game_text='Return Dunsparce and all cards attached to it to your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
