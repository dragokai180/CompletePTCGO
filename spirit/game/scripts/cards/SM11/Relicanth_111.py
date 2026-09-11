from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9134ae3b-ca6c-56d0-9011-4616db977517',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Relicanth.Name',
    display_name='Relicanth',
    searchable_by=['Relicanth', 'Basic', 'Relicanth'],
    subtypes=['Basic'],
    collector_number=111,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=369,
    abilities=[
        Attack(
            title='Deep Sea Boring',
            game_text='Search your deck for a Trainer card, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Water Pulse',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
