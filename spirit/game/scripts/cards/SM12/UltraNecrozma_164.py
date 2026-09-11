from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5b28e8c3-8f98-589a-8c88-d7f4871047c1',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.UltraNecrozma.Name',
    display_name='Ultra Necrozma',
    searchable_by=['Ultra Necrozma', 'Basic', 'Ultra Beast', 'UltraNecrozma'],
    subtypes=['Basic', 'Ultra Beast'],
    collector_number=164,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=800,
    abilities=[
        Ability(
            title='Ultra Burst',
            game_text="This Pokémon can't attack unless your opponent has 2 or fewer Prize cards remaining.",
            passive=standard_passive("This Pokémon can't attack unless your opponent has 2 or fewer Prize cards remaining."),
        ),
        Attack(
            title='Luster of Downfall',
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
