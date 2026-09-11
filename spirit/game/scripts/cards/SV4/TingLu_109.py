from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='55d31782-0ebd-5758-b873-27e797b1ec4c',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TingLu.Name',
    display_name='Ting-Lu',
    searchable_by=['Ting-Lu', 'Basic', 'TingLu'],
    subtypes=['Basic'],
    collector_number=109,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=1003,
    abilities=[
        Attack(
            title='Sand Bringer',
            game_text='Attach up to 2 Basic Fighting Energy cards from your discard pile to 1 of your Pokémon.',
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Arrogant Impact',
            game_text='If this Pokémon has 4 or more damage counters on it, this attack does nothing.',
            cost={PokemonTypes.FIGHTING: 3},
            damage=220,
            effect=standard_attack,
        ),
    ],
)
