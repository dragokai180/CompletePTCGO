from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b9652670-d363-5688-973b-0b795f478dea',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name',
    display_name='Muk',
    searchable_by=['Muk', 'Stage 1', 'Muk'],
    subtypes=['Stage 1'],
    collector_number=127,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name',
    family_id=88,
    abilities=[
        Ability(
            title='Poison Sacs',
            game_text="Your opponent's Poisoned Pokémon don't recover from that Special Condition when they evolve or devolve.",
            passive=standard_passive("Your opponent's Poisoned Pokémon don't recover from that Special Condition when they evolve or devolve."),
        ),
        Attack(
            title='Toxic Strike',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
