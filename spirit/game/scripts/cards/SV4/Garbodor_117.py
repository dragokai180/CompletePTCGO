from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dd50ae07-ecda-5204-a8db-2cd2c277aad2',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name',
    display_name='Garbodor',
    searchable_by=['Garbodor', 'Stage 1', 'Garbodor'],
    subtypes=['Stage 1'],
    collector_number=117,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name',
    family_id=568,
    abilities=[
        Attack(
            title='Chuck',
            game_text='Discard any number of Pokémon Tool cards from your hand. This attack does 50 damage for each card you discarded in this way.',
            cost={PokemonTypes.DARKNESS: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Venomous Hit',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
