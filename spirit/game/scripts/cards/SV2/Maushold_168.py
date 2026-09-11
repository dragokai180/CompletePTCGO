from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0f73fe60-2816-599b-8e8b-da23615938c6',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Maushold.Name',
    display_name='Maushold',
    searchable_by=['Maushold', 'Stage 1', 'Maushold'],
    subtypes=['Stage 1'],
    collector_number=168,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name',
    family_id=924,
    abilities=[
        Attack(
            title='Gentle Slap',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title='Gnaw Relentlessly',
            game_text="Put 1 damage counter on each of your opponent's Pokémon for each of your Maushold in play.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
