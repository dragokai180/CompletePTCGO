from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a4486130-00c2-5a63-9bd6-fcf1203fbdf6',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanClodsire.Name',
    display_name='Paldean Clodsire',
    searchable_by=['Paldean Clodsire', 'Stage 1', 'PaldeanClodsire'],
    subtypes=['Stage 1'],
    collector_number=128,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name',
    family_id=194,
    abilities=[
        Attack(
            title='Poison Ring',
            game_text="Your opponent's Active Pokémon is now Poisoned. During your opponent's next turn, that Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Muddy Hammer',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
