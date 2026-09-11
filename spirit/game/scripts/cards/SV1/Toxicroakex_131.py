from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='25acf927-d47e-5796-a808-af034197be43',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroakex.Name',
    display_name='Toxicroak ex',
    searchable_by=['Toxicroak ex', 'Stage 1', 'ex', 'Toxicroakex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=131,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name',
    family_id=453,
    abilities=[
        Attack(
            title='Nasty Plot',
            game_text='Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Toxic Ripper',
            game_text="Your opponent's Active Pokémon is now Poisoned. During Pokémon Checkup, put 6 damage counters on that Pokémon instead of 1.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
