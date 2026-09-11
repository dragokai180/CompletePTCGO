from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='12194ece-adf1-5de5-b293-8a8df381550a',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name',
    display_name='Poliwhirl',
    searchable_by=['Poliwhirl', 'Stage 1', 'Poliwhirl'],
    subtypes=['Stage 1'],
    collector_number=37,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name',
    family_id=60,
    abilities=[
        Attack(
            title='Hypnoblast',
            game_text='The Defending Pokémon is now Asleep.',
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Light Punch',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
