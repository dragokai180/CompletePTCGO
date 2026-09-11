from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='821999f7-a613-57ec-b804-0371ff461943',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name',
    display_name='Palkia',
    searchable_by=['Palkia', 'Basic', 'Palkia'],
    subtypes=['Basic'],
    collector_number=40,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=484,
    abilities=[
        Attack(
            title='Teleportation Burst',
            game_text='You may switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Prize Count',
            game_text='If you have more Prize cards remaining than your opponent, this attack does 80 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
